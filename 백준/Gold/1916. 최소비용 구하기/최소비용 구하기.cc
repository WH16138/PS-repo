#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 1000000000;

int main() {
    int n, m, start, end;
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n + 1);

    for (int i = 0; i < m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].push_back(make_pair(b, w));
    }

    cin >> start >> end;

    vector<int> dist(n + 1, INF);
    dist[start] = 0;
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, start));

    while (!pq.empty()) {
        int current_dist = pq.top().first;
        int current = pq.top().second;
        pq.pop();

        if (current_dist > dist[current])
            continue;

        for (int i = 0; i < graph[current].size(); i++) {
            int next = graph[current][i].first;
            int cost = current_dist + graph[current][i].second;

            if (cost < dist[next]) {
                dist[next] = cost;
                pq.push(make_pair(cost, next));
            }
        }
    }

    cout << dist[end];

    return 0;
}