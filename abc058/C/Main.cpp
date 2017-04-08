#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	int c[26];
	for(int i = 0; i < 26; i++) {
		c[i] = 10000;
	}
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		char s[51];
		scanf("%s", s);
		int ci[26] = {};
		for(int j = 0; j < strlen(s); j++) {
			ci[s[j] - 'a']++;
		}
		for(int j = 0; j < 26; j++) {
			c[j] = min(c[j], ci[j]);
		}
	}
	for(int i = 0; i < 26; i++) {
		for(int j = c[i]; j > 0; j--) {
			printf("%c", 'a' + i);
		}
	}
	printf("\n");
	return 0;
}
