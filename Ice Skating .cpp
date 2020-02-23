#include <iostream>
#include <vector>
using namespace std;
int vizitate=0;
void dfs(int nod,vector<int> &viz, vector<vector<int>> &Graf)
{
    viz[nod]=1;
    vizitate++;
    for(auto i:Graf[nod])
    {
        if(viz[i]==0)
            dfs(i,viz,Graf);
    }
}
int main()
{
    int n;
    cin>>n;
    vector <pair<int,int>>Noduri(n+1);
    vector<int> viz(n+1,0);
    for(int i=1;i<=n;i++)
    {
        int x,y;
        cin>>x>>y;
        Noduri[i]={x,y};
    }
    vector<vector<int>> Graf(n+1);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if(i!=j)
            {
                int a=Noduri[i].first,b=Noduri[i].second,c=Noduri[j].first,d=Noduri[j].second;
                if(Noduri[i].first==Noduri[j].first || Noduri[i].second==Noduri[j].second)
                {
                    Graf[i].push_back(j);
                }
            }
        }
    }
    int nr_comp=0;
    while(vizitate<n)
    {
        for(int i=1;i<=n;i++)
        {
            if(viz[i]==0)
            {
                nr_comp++;
                dfs(i,viz,Graf);
            }
        }
    }
    cout<<nr_comp-1;
}
