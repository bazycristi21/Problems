#include <vector>
#include <fstream>
#include <cmath>
#include <map>
#include <iomanip>
#include <set>
using namespace std;

ifstream in("retea2.in");
ofstream out("retea2.out");
struct nod
{
    int x,y;
};
double d(pair<long long int,long long int> X, pair<long long int,long long int> Y)
{
    return sqrt((Y.first-X.first)*(Y.first-X.first)+(Y.second-X.second)*(Y.second-X.second));
}

int main()
{
    int N,M;
    in>>N>>M;
    vector < pair< long long int, long long int>> G;
	vector < int > viz(N + M + 1, 0);
	vector <double> dist(4000, 10000000000.0l);
	set < pair< double, int>> S;

    for(int i=0;i<N+M;i++)
    {
        int x,y;
        in>>x>>y;
        G.push_back({x,y});
    }

    for(int i=N;i<N+M;i++)
    {
        for(int j=0;j<N;j++)
        {
            double aux=d(G[i],G[j]);
            if(aux<dist[i])
                dist[i]=aux;
        }
        S.insert({dist[i],i});
    }
    int nr=0;
    double suma=0.0;
    while(nr<M)
    {
        auto p=(*S.begin());
        S.erase(S.begin());
        if(viz[p.second]==0)
        {
            nr++;
            viz[p.second]=1;
            suma=suma+p.first;
            for(int i=N;i<N+M;i++)
            {
                auto x=G[i];
                double cost=d(G[p.second],x);
                if(cost<dist[i] && viz[i]==0)
                {
                    dist[i]=cost;
                    S.insert({dist[i],i});
                }
            }
        }
    }
    out<<fixed<<setprecision(6)<<suma;
    return 0;
}
