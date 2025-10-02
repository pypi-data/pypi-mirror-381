#ifndef DUNE_VEM_SPACE_INDEXSET_HH
#define DUNE_VEM_SPACE_INDEXSET_HH

#include <cassert>
#include <cstddef>

#include <algorithm>
#include <numeric>
#include <utility>
#include <vector>

#include <dune/grid/common/rangegenerators.hh>

#include <dune/vem/agglomeration/agglomeration.hh>
#include <dune/vem/agglomeration/boundingbox.hh>
#include <dune/vem/agglomeration/indexset.hh>
#include <dune/vem/misc/vector.hh>

namespace Dune
{

  namespace Vem
  {

    // AgglomerationIndexSet
    // ---------------------

    template< class GridPart, class Allocator = std::allocator< std::size_t > >
    using VemAgglomerationIndexSet = AgglomerationIndexSet< GridPart, Allocator >;
#if 0
    {
      typedef VemAgglomerationIndexSet< GridPart, Allocator > ThisType;
      typedef AgglomerationIndexSet< GridPart, Allocator > BaseType;

    public:
      // !TS
      typedef GridPart GridPartType;

      typedef typename BaseType::AgglomerationType AgglomerationType;
      typedef typename BaseType::AllocatorType AllocatorType;

      // !TS assume vector of vectors
      explicit VemAgglomerationIndexSet ( AgglomerationType &agglomeration,
          AllocatorType allocator = AllocatorType() )
      : BaseType( agglomeration, allocator )
      {}
      using BaseType::update;

      Std::vector<int> orders()
      {
        /*
        Std::vector<int> ret(3,0);
        ret[0] += testSpaces_[2][0];
        ret[1] += std::min( {testSpaces_[2][0] + 1, edgeDegrees()[0]} );
        ret[2] += std::min( {testSpaces_[2][0] + 2, edgeDegrees()[0]+1, edgeDegrees()[1]} );
        return ret;
        */
      }

      const Std::vector<int> maxDegreePerCodim() const
      {
        /*
        Std::vector<int> ret(3);
          for ( int k = 0; k < ret.size(); k++){
            ret[k] = *std::max_element( testSpaces_[k].begin(), testSpaces_[k].end() );
          }
         return ret;
       */
      }

      Std::vector<int> edgeDegrees() const
      {
        /*
        assert( testSpaces_[2].size()<2 );
        Std::vector<int> degrees(2, -1);
        for (std::size_t i=0;i<testSpaces_[0].size();++i)
          degrees[i] += 2*(testSpaces_[0][i]+1);
        if (testSpaces_[0].size()>1 && testSpaces_[0][1]>-1) // add tangential derivatives
          degrees[0] += 2;
        for (std::size_t i=0;i<testSpaces_[1].size();++i)
          degrees[i] += std::max(0,testSpaces_[1][i]+1);
        return degrees;
        */
      }
      std::size_t edgeSize(int deriv) const
      {
        auto degrees = edgeDegrees();
        return degrees[deriv] < 0 ? 0 :
              Dune::Fem::OrthonormalShapeFunctions<1>::size( degrees[deriv] );
      }
      std::size_t maxEdgeDegree() const
      {
        auto degrees = edgeDegrees();
        return *std::max_element(degrees.begin(),degrees.end());
      }

      const std::vector<int> vertexOrders() const
      {
        // return testSpaces_[0];
      }

      const std::vector<int> edgeOrders() const
      {
        // return testSpaces_[1];
      }

      const std::vector<int> innerOrders() const
      {
        // return testSpaces_[2];
      }

      template <int dim>
      std::size_t order2size(unsigned int deriv) const
      {
      /*
        if (testSpaces_[dim].size()<=deriv || testSpaces_[dim][deriv]<0)
          return 0;
        else
        {
          if constexpr (dim>0)
            return Dune::Fem::OrthonormalShapeFunctions<dim>::
              size(testSpaces_[dim][deriv]);
          else
            return pow(BaseType::dimension,deriv);
        }
      */
      }


    private:
      std::size_t sumTestSpaces(unsigned int codim) const
      {
        // return std::accumulate(testSpaces_[codim].begin(),testSpaces_[codim].end(),0);
      }
    };
#endif

  } // namespace Vem

} // namespace Dune

#endif // #ifndef DUNE_VEM_AGGLOMERATION_INDEXSET_HH
