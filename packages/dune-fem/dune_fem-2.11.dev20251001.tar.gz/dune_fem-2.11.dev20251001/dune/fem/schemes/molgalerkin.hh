#ifndef DUNE_FEM_SCHEMES_MOLGALERKIN_HH
#define DUNE_FEM_SCHEMES_MOLGALERKIN_HH

// fem includes
#include <dune/fem/schemes/galerkin.hh>
#include <dune/fem/function/localfunction/temporary.hh>
#include <dune/fem/common/bindguard.hh>

namespace Dune
{

  namespace Fem
  {

#if HAVE_PETSC
    //forward declaration of PetscLinearOperator
    template <typename DomainFunction, typename RangeFunction >
    class PetscLinearOperator ;
#endif

    // GalerkinOperator
    // ----------------

    template< class Integrands, class DomainFunction, class RangeFunction = DomainFunction >
    struct MOLGalerkinOperator
      : public virtual Operator< DomainFunction, RangeFunction >
    {
      typedef DomainFunction DomainFunctionType;
      typedef RangeFunction RangeFunctionType;


      static_assert( std::is_same< typename DomainFunctionType::GridPartType, typename RangeFunctionType::GridPartType >::value, "DomainFunction and RangeFunction must be defined on the same grid part." );

      typedef typename RangeFunctionType::GridPartType GridPartType;
      typedef ThreadIterator< GridPartType >  ThreadIteratorType;

      typedef Impl::GalerkinOperator< GridPartType >    GalerkinOperatorImplType;
      typedef Impl::LocalGalerkinOperator< Integrands > LocalGalerkinOperatorImplType;

      typedef typename RangeFunctionType :: DiscreteFunctionSpaceType   DiscreteFunctionSpaceType;

      typedef typename LocalGalerkinOperatorImplType::template QuadratureSelector<
            DiscreteFunctionSpaceType > :: InteriorQuadratureType    InteriorQuadratureType;

      typedef LocalMassMatrix< DiscreteFunctionSpaceType, InteriorQuadratureType >  LocalMassMatrixType ;

      template< class... Args >
      explicit MOLGalerkinOperator ( const GridPartType &gridPart, Args &&... args )
        : iterators_( gridPart ),
          opImpl_( gridPart ),
          localOp_( gridPart, std::forward< Args >( args )... ),
          gridSizeInterior_( 0 ),
          communicate_( true )
      {
      }

      void setCommunicate( const bool communicate )
      {
        communicate_ = communicate;
        if( ! communicate_ && Dune::Fem::Parameter::verbose() )
        {
          std::cout << "MOLGalerkinOperator::setCommunicate: communicate was disabled!" << std::endl;
        }
      }

      void setQuadratureOrders(unsigned int interior, unsigned int surface)
      {
        size_t size = localOp_.size();
        for( size_t i=0; i<size; ++i )
          localOp_[ i ].setQuadratureOrders(interior,surface);
      }

      virtual void operator() ( const DomainFunctionType &u, RangeFunctionType &w ) const final override
      {
        evaluate( u, w );
      }

      template< class GridFunction >
      void operator() ( const GridFunction &u, RangeFunctionType &w ) const
      {
        evaluate( u, w );
      }

      const GridPartType &gridPart () const { return op().gridPart(); }

      typedef Integrands ModelType;
      typedef Integrands DirichletModelType;
      ModelType &model() const { return localOperator().model(); }

      [[deprecated("Use localOperator instead!")]]
      const GalerkinOperatorImplType& impl() const { return localOperator(); }

      const LocalGalerkinOperatorImplType& localOperator() const { return (*localOp_); }

      std::size_t gridSizeInterior () const { return gridSizeInterior_; }

    protected:
      const GalerkinOperatorImplType& op() const { return (*opImpl_); }

      template <class Iterators>
      void applyInverseMass( const Iterators& iterators, RangeFunctionType& w ) const
      {
        // temporary local function
        typedef TemporaryLocalFunction< typename RangeFunctionType::DiscreteFunctionSpaceType > TemporaryLocalFunctionType;
        TemporaryLocalFunctionType wLocal( w.space() );
        LocalMassMatrixType localMassMatrix( w.space(), localOperator().interiorQuadratureOrder( w.space().order() ) );

        // iterate over all elements (in the grid or per thread)
        // thread safety is guaranteed through discontinuous data (spaces)
        for( const auto& entity : iterators )
        {
          // obtain local function
          auto guard = bindGuard( wLocal, entity );
          // obtain local dofs
          w.getLocalDofs( entity, wLocal.localDofVector() );

          // apply inverse mass matrix
          // TODO: add mass term if needed (from ufl expression)
          localMassMatrix.applyInverse( entity, wLocal );

          // overwrite dofs in discrete function
          w.setLocalDofs( entity, wLocal.localDofVector() );
        }
      }

      template< class GridFunction >
      void evaluate( const GridFunction &u, RangeFunctionType &w ) const
      {
        iterators_.update();
        w.clear();

        std::shared_mutex mutex;

        auto doEval = [this, &u, &w, &mutex] ()
        {
          // version with locking
          std::tuple< const LocalGalerkinOperatorImplType& > integrands( localOperator() );
          this->op().evaluate( u, w, this->iterators_, integrands, mutex );

          // version without locking
          //RangeFunctionType wTmp( w );
          //this->op().evaluate( u, wTmp, this->iterators_ );
          //std::lock_guard guard ( mutex );
          //w += wTmp;
        };

        bool singleThreadModeError = false ;

        try {
          // execute in parallel
          MPIManager :: run ( doEval );

          // update grid size interior
          gridSizeInterior_ = Impl::accumulateGridSize( opImpl_ );
        }
        catch ( const SingleThreadModeError& e )
        {
          singleThreadModeError = true;
        }

        // method of lines
        auto doInvMass = [this, &w] ()
        {
          this->applyInverseMass( this->iterators_, w );
        };

        if( ! singleThreadModeError )
        {
          try {
            // execute in parallel
            MPIManager :: run ( doInvMass );
          }
          catch ( const SingleThreadModeError& e )
          {
            singleThreadModeError = true;
          }
        }

        // if error occurred, redo the whole evaluation
        if( singleThreadModeError )
        {
          // reset w from previous entries
          w.clear();
          // re-run in single thread mode if previous attempt failed
          std::tuple< const LocalGalerkinOperatorImplType& > integrands( localOperator() );
          op().evaluate( u, w, iterators_, integrands );

          // update number of interior elements as sum over threads
          gridSizeInterior_ = Impl::accumulateGridSize( opImpl_ );

          applyInverseMass( iterators_, w );
        }

        // synchronize data
        if( communicate_ )
          w.communicate();
      }

      // GalerkinOperator implementation (see galerkin.hh)
      mutable ThreadIteratorType iterators_;
      ThreadSafeValue< GalerkinOperatorImplType > opImpl_;
      ThreadSafeValue< LocalGalerkinOperatorImplType > localOp_;

      mutable std::size_t gridSizeInterior_;
      bool communicate_;
    };



    // DifferentiableGalerkinOperator
    // ------------------------------

    template< class Integrands, class JacobianOperator >
    class MOLDifferentiableGalerkinOperator
      : public MOLGalerkinOperator< Integrands, typename JacobianOperator::DomainFunctionType, typename JacobianOperator::RangeFunctionType >,
        public DifferentiableOperator< JacobianOperator >
    {
     typedef MOLGalerkinOperator< Integrands, typename JacobianOperator::DomainFunctionType, typename JacobianOperator::RangeFunctionType > BaseType;

    public:
      typedef JacobianOperator JacobianOperatorType;

      typedef typename BaseType::DomainFunctionType DomainFunctionType;
      typedef typename BaseType::RangeFunctionType RangeFunctionType;
      typedef typename DomainFunctionType::DiscreteFunctionSpaceType DomainDiscreteFunctionSpaceType;
      typedef typename RangeFunctionType::DiscreteFunctionSpaceType RangeDiscreteFunctionSpaceType;

      typedef typename BaseType::LocalGalerkinOperatorImplType    LocalGalerkinOperatorImplType;

      typedef DiagonalAndNeighborStencil< DomainDiscreteFunctionSpaceType, RangeDiscreteFunctionSpaceType >  DiagonalAndNeighborStencilType;
      typedef DiagonalStencil< DomainDiscreteFunctionSpaceType, RangeDiscreteFunctionSpaceType >             DiagonalStencilType;

      typedef typename BaseType::GridPartType GridPartType;

      template< class... Args >
      explicit MOLDifferentiableGalerkinOperator ( const DomainDiscreteFunctionSpaceType &dSpace,
                                                   const RangeDiscreteFunctionSpaceType &rSpace,
                                                   Args &&... args )
        : BaseType( rSpace.gridPart(), std::forward< Args >( args )... ),
          dSpace_(dSpace),
          rSpace_(rSpace),
          domainSpaceSequence_(dSpace.sequence()),
          rangeSpaceSequence_(rSpace.sequence()),
          stencilDAN_(), stencilD_()
      {
        if( hasSkeleton() )
          stencilDAN_.reset( new DiagonalAndNeighborStencilType( dSpace_, rSpace_ ) );
        else
          stencilD_.reset( new DiagonalStencilType( dSpace_, rSpace_ ) );
      }

      virtual void jacobian ( const DomainFunctionType &u, JacobianOperatorType &jOp ) const final override
      {
        // assemble Jacobian, same as GalerkinOperator
        assemble( u, jOp );
      }

      template< class GridFunction >
      void jacobian ( const GridFunction &u, JacobianOperatorType &jOp ) const
      {
        assemble( u, jOp );
      }

      const DomainDiscreteFunctionSpaceType& domainSpace() const
      {
        return dSpace_;
      }
      const RangeDiscreteFunctionSpaceType& rangeSpace() const
      {
        return rSpace_;
      }
      // needed for DGHelmholtz operator
      const RangeDiscreteFunctionSpaceType& space() const
      {
        return rangeSpace();
      }

      using BaseType::gridPart;
      using BaseType::localOperator;

    protected:
      using BaseType::op;
      using BaseType::iterators_;
      using BaseType::gridSizeInterior_;

      //! returns true if one of the models has a skeleton term
      bool hasSkeleton() const
      {
        std::tuple< const LocalGalerkinOperatorImplType& > integrands( localOperator() );
        return op().hasSkeleton( integrands );
      }

      void prepare( JacobianOperatorType& jOp ) const
      {
        if ( domainSpaceSequence_ != domainSpace().sequence()
             || rangeSpaceSequence_ != rangeSpace().sequence() )
        {
          domainSpaceSequence_ = domainSpace().sequence();
          rangeSpaceSequence_ = rangeSpace().sequence();
          if( hasSkeleton() )
          {
            assert( stencilDAN_ );
            stencilDAN_->update();
          }
          else
          {
            assert( stencilD_ );
            stencilD_->update();
          }
        }

        if( hasSkeleton() )
          jOp.reserve( *stencilDAN_ );
        else
          jOp.reserve( *stencilD_ );
        // set all entries to zero
        jOp.clear();
      }

      template < class GridFunction >
      void assemble( const GridFunction &u, JacobianOperatorType &jOp ) const
      {
        prepare( jOp );
        iterators_.update();

        bool singleThreadModeError = false;
        std::shared_mutex mutex;

        auto doAssemble = [this, &u, &jOp, &mutex] ()
        {
          std::tuple< const LocalGalerkinOperatorImplType& > integrands( localOperator() );
          // assemble Jacobian, same as GalerkinOperator
          this->op().assemble( u, jOp, this->iterators_, integrands, mutex );
        };

        try {
          // execute in parallel
          MPIManager :: run ( doAssemble );

          // update number of interior elements as sum over threads
          gridSizeInterior_ = Impl::accumulateGridSize( this->opImpl_ );
        }
        catch ( const SingleThreadModeError& e )
        {
          singleThreadModeError = true;
        }

        if (!singleThreadModeError)
        {
          GetSetLocalMatrix< JacobianOperatorType > getSet( jOp );

          // method of lines
          auto doInvMass = [this, &getSet] ()
          {
            applyInverseMass( this->iterators_, getSet, this->hasSkeleton() );
          };

          try {
            // execute in parallel
            MPIManager :: run ( doInvMass );
          }
          catch ( const SingleThreadModeError& e )
          {
            singleThreadModeError = true;
          }
        }

        if (singleThreadModeError)
        {
          // redo matrix assembly since it failed
          jOp.clear();
          std::tuple< const LocalGalerkinOperatorImplType& > integrands( localOperator() );
          op().assemble( u, jOp, iterators_, integrands );

          // update number of interior elements as sum over threads
          gridSizeInterior_ = Impl::accumulateGridSize( this->opImpl_ );

          GetSetLocalMatrixImpl getSet( jOp );

          // apply inverse mass
          applyInverseMass( iterators_, getSet, hasSkeleton() );
        }

        // note: assembly done without local contributions so need
        // to call flush assembly
        jOp.flushAssembly();
      }


      struct GetSetLocalMatrixImpl
      {
        JacobianOperatorType& jOp_;
        GetSetLocalMatrixImpl( JacobianOperatorType& jOp ) : jOp_( jOp ) {}

        template <class Entity, class LocalMatrix>
        void getLocalMatrix( const Entity& domainEntity, const Entity& rangeEntity,
                             LocalMatrix& lop ) const
        {
          jOp_.getLocalMatrix( domainEntity, rangeEntity, lop );
        }

        template <class Entity, class LocalMatrix>
        void setLocalMatrix( const Entity& domainEntity, const Entity& rangeEntity,
                             const LocalMatrix& lop )
        {
          jOp_.setLocalMatrix( domainEntity, rangeEntity, lop );
        }
      };

      struct GetSetLocalMatrixImplLocked : public GetSetLocalMatrixImpl
      {
        typedef GetSetLocalMatrixImpl BaseType;
        typedef std::shared_mutex mutex_t;
        mutable mutex_t mutex_;

        GetSetLocalMatrixImplLocked( JacobianOperatorType &jOp ) : BaseType( jOp ) {}

        template <class Entity, class LocalMatrix>
        void getLocalMatrix( const Entity& domainEntity, const Entity& rangeEntity,
                             LocalMatrix& lop ) const
        {
          std::lock_guard< mutex_t > lock( mutex_ );
          BaseType::getLocalMatrix( domainEntity, rangeEntity, lop );
        }

        template <class Entity, class LocalMatrix>
        void setLocalMatrix( const Entity& domainEntity, const Entity& rangeEntity,
                             const LocalMatrix& lop )
        {
          std::lock_guard< mutex_t > lock( mutex_ );
          BaseType::setLocalMatrix( domainEntity, rangeEntity, lop );
        }
      };

      template <class JacOp>
      struct GetSetLocalMatrix : public GetSetLocalMatrixImpl
      {
        typedef GetSetLocalMatrixImpl BaseType;
        GetSetLocalMatrix( JacobianOperatorType &jOp ) : BaseType( jOp ) {}
      };

#if HAVE_PETSC
      //- PetscLinearOperator does not work with threaded applyInverseMass
      //- because the mix of getLocalMatrix and setLocalMatrix seems to be
      //- problematic. Therefore we used the locked version.
      template <class DomainFunction, class RangeFunction>
      struct GetSetLocalMatrix< PetscLinearOperator< DomainFunction, RangeFunction > > : public GetSetLocalMatrixImplLocked
      {
        typedef GetSetLocalMatrixImplLocked BaseType;
        GetSetLocalMatrix( JacobianOperatorType &jOp ) : BaseType( jOp ) {}
      };
#endif

      template <class Iterators, class GetSetLocalMatrixOp >
      void applyInverseMass ( const Iterators& iterators, GetSetLocalMatrixOp& getSet,
                              const bool hasSkeleton ) const
      {
        typedef typename BaseType::LocalMassMatrixType  LocalMassMatrixType;
        JacobianOperatorType& jOp = getSet.jOp_;

        LocalMassMatrixType localMassMatrix( jOp.rangeSpace(), localOperator().interiorQuadratureOrder( jOp.rangeSpace().order() ) );

        TemporaryLocalMatrix< DomainDiscreteFunctionSpaceType, RangeDiscreteFunctionSpaceType >
                  lop(jOp.domainSpace(), jOp.rangeSpace());

        // multiply with inverse mass matrix
        for( const auto& inside : iterators )
        {
          // scale diagonal
          {
            auto guard = bindGuard( lop, inside,inside );
            lop.bind(inside,inside);
            getSet.getLocalMatrix( inside, inside, lop );
            localMassMatrix.leftMultiplyInverse( lop );
            getSet.setLocalMatrix( inside, inside, lop );
          }

          if( hasSkeleton )
          {
            for( const auto &intersection : intersections( gridPart(), inside ) )
            {
              // scale off-diagonal
              if( intersection.neighbor() )
              {
                const auto& outside = intersection.outside();
                auto guard = bindGuard( lop, outside,inside );
                getSet.getLocalMatrix( outside, inside, lop );
                localMassMatrix.leftMultiplyInverse( lop );
                getSet.setLocalMatrix( outside, inside, lop );
              }
            }
          }
        }
      }

      const DomainDiscreteFunctionSpaceType &dSpace_;
      const RangeDiscreteFunctionSpaceType &rSpace_;
      mutable int domainSpaceSequence_, rangeSpaceSequence_;

      mutable std::unique_ptr< DiagonalAndNeighborStencilType > stencilDAN_;
      mutable std::unique_ptr< DiagonalStencilType >            stencilD_;
    };



    // AutomaticDifferenceGalerkinOperator
    // -----------------------------------

    template< class Integrands, class DomainFunction, class RangeFunction >
    class MOLAutomaticDifferenceGalerkinOperator
      : public MOLGalerkinOperator< Integrands, DomainFunction, RangeFunction >,
        public AutomaticDifferenceOperator< DomainFunction, RangeFunction >
    {
      typedef MOLGalerkinOperator< Integrands, DomainFunction, RangeFunction > BaseType;
      typedef AutomaticDifferenceOperator< DomainFunction, RangeFunction > AutomaticDifferenceOperatorType;

    public:
      typedef typename BaseType::GridPartType GridPartType;

      template< class... Args >
      explicit MOLAutomaticDifferenceGalerkinOperator ( const GridPartType &gridPart, Args &&... args )
        : BaseType( gridPart, std::forward< Args >( args )... ), AutomaticDifferenceOperatorType()
      {}
    };



    // ModelDifferentiableGalerkinOperator
    // -----------------------------------

    template < class LinearOperator, class ModelIntegrands >
    struct MOLModelDifferentiableGalerkinOperator
      : public MOLDifferentiableGalerkinOperator< ModelIntegrands, LinearOperator >
    {
      typedef MOLDifferentiableGalerkinOperator< ModelIntegrands, LinearOperator > BaseType;

      typedef typename ModelIntegrands::ModelType ModelType;

      typedef typename LinearOperator::DomainFunctionType RangeFunctionType;
      typedef typename LinearOperator::RangeSpaceType DiscreteFunctionSpaceType;

      MOLModelDifferentiableGalerkinOperator ( ModelType &model, const DiscreteFunctionSpaceType &dfSpace )
        : BaseType( dfSpace.gridPart(), model )
      {}

      template< class GridFunction >
      void apply ( const GridFunction &u, RangeFunctionType &w ) const
      {
        (*this)( u, w );
      }

      template< class GridFunction >
      void apply ( const GridFunction &u, LinearOperator &jOp ) const
      {
        (*this).jacobian( u, jOp );
      }
    };


    // MethodOfLinesScheme
    // -------------------

    template< class Integrands, class LinearOperator, class InverseOperator, bool addDirichletBC>
    using MethodOfLinesScheme = Impl::GalerkinSchemeImpl< Integrands, LinearOperator, InverseOperator, addDirichletBC,
                                                          MOLDifferentiableGalerkinOperator >;

  } // namespace Fem

} // namespace Dune

#endif // #ifndef DUNE_FEM_SCHEMES_MOLGALERKIN_HH
