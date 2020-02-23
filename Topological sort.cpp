#include <fstream>
#include <vector>
#include <queue>
using namespace std;
ifstream in("sortaret.in");
ofstream out("sortaret.out");

int main()
{
    int n,m;
    in>>n>>m;
    vector <vector<int>> G(n+1);
    int grad[n+1]={0};
    queue <int> q;
    int i;
    for(i=1;i<=m;i++)
    {
        int x,y;
        in>>x>>y;
        G[x].push_back(y);
        grad[y]++;
    }
    for(i=1;i<=n;i++)
    {
        if(grad[i]==0)
            q.push(i);
    }
    while(!q.empty())
    {
        out<<q.front()<<" ";
        int p=q.front();
        q.pop();
        for(auto j: G[p])
        {
            grad[j]--;
            if(grad[j]==0)
                q.push(j);
        }
    }



}
