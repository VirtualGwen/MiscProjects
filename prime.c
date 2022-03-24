#include <stdio.h>

int main() {

	unsigned long long n;
	int i;
	int flag = 0;

	printf("Enter a positive integer: ");
	scanf("%llu", &n);

	if (n == 0 || n == 1)
		flag = 1;

	for (i = 2; i <= n / 2; ++i) {

		if (n % i == 0) {
			flag = 1;
			break;
		}
	}

	if (flag == 0)
		printf("%llu is a prime number.", n);

	else
		printf("%llu is not a prime number.", n);

	return 0;
}
