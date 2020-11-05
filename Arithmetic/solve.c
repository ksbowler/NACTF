#include <stdio.h>
#include <stdint.h>

int main() {
	int64_t a;
	for (a=0;;a++) {
		if ((uint32_t) a + (uint32_t) 2718281828 == 42) {
			printf("%lld",a);
			break;
		}
	}
}
