#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	int ss[100001];
	int ts[100001];
	char s[100001];
	char t[100001];
	scanf("%s%s", s, t);
	ss[0] = 0;
	ts[0] = 0;
	for(int i = 0, ls = strlen(s); i < ls; i++) {
		if (s[i] == 'A') {
			ss[i + 1] = (ss[i] + 1) % 3;
		} else {
			ss[i + 1] = (ss[i] + 2) % 3;
		}
	}
	for(int i = 0, lt = strlen(t); i < lt; i++) {
		if (t[i] == 'A') {
			ts[i + 1] = (ts[i] + 1) % 3;
		} else {
			ts[i + 1] = (ts[i] + 2) % 3;
		}
	}
	int q;
	scanf("%d", &q);
	for(int i = 0; i < q; i++) {
		int a, b, c, d;
		scanf("%d%d%d%d", &a, &b, &c, &d);
		if (((ss[b] - ss[a - 1]) - (ts[d] - ts[c - 1])) % 3 == 0) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
