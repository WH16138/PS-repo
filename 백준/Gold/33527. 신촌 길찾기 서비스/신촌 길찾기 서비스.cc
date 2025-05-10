#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X;
    cin >> N >> X;
    int V = 5 * X;

    vector<vector<int>> dist(V, vector<int>(V, INF));
    vector<vector<int>> station(N+1);

    for(int i = 0; i < V; i++){
        dist[i][i] = 0;
    }

    for(int num = 1; num <= N; num++){
        int a, b, c, d, e;
        cin >> a >> b >> c >> d >> e;
        int stops[5] = {a, b, c, d, e};
        for(int i = 0; i < 5; i++){
            int idx = stops[i] + i * X - 1;
            station[num].push_back(idx);
        }
        for(int i = 0; i < 5; i++){
            for(int j = 0; j < 5; j++){
                if(i == j) continue;
                int u = station[num][i];
                int v = station[num][j];
                dist[u][v] = 1;
            }
        }
    }

    for(int k = 0; k < V; k++){
        for(int i = 0; i < V; i++){
            if(dist[i][k] == INF) continue;
            for(int j = 0; j < V; j++){
                if(dist[k][j] == INF) continue;
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    int Q;
    cin >> Q;
    while(Q--){
        int u, v;
        cin >> u >> v;
        bool shared = false;
        for(int su : station[u]){
            for(int sv : station[v]){
                if(su == sv){
                    shared = true;
                    break;
                }
            }
            if(shared) break;
        }
        if(shared){
            cout << 1 << "\n";
            continue;
        }
        int best = INF;
        for(int su : station[u]){
            for(int sv : station[v]){
                if(dist[su][sv] < INF){
                    best = min(best, dist[su][sv] + 1);
                }
            }
        }
        cout << (best == INF ? -1 : best) << "\n";
    }
    return 0;
}