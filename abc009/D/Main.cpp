#include <cstdint>
#include <cstddef>
#include <vector>
#include <iostream>

typedef std::uint32_t T;
class M {
    std::size_t row;
    std::size_t column;

   private:
    std::vector<T> d;

   public:
    M(std::size_t row_, std::size_t column_)
        : row(row_), column(column_), d(row_ * column_) {}

    T& operator()(std::size_t i, std::size_t j) { return d[i * column + j]; }
    const T& operator()(std::size_t i, std::size_t j) const { return d[i * column + j]; }
    M& operator*=(const M& rhs) {
        M a(this->row, rhs.column);
        for (std::size_t i = 0; i < this->row; i++) {
            for (std::size_t j = 0; j < rhs.column; j++) {
                T o = 0;
                for (std::size_t k = 0; k < this->column; k++) {
                    o ^= (*this)(i, k) & rhs(k, j);
                }
                a(i, j) = o;
            }
        }
        *this = a;
        return *this;
    }
    friend M operator*(M lhs, const M& rhs) {
        lhs *= rhs;
        return lhs;
    }
    M pow(std::size_t n) {
        M r = Id(this->row);
        M a = *this;
        for (; n != 0; n >>= 1) {
            if (n & 1) {
                r *= a;
            }
            a *= a;
        }
        return r;
    }
    static M Id(std::size_t n) {
        M a(n, n);
        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < n; j++) {
                a(i, j) = (i == j) ? 0xFFFFFFFF : 0;
            }
        }
        return a;
    }
};

int main() {
    std::size_t k, m;
    std::cin >> k >> m;
    M a(k, 1);
    M p(k, k);
    for (std::size_t i = 0; i < k; i++) {
        std::cin >> a(i, 0);
    }
    for (std::size_t i = 0; i < k; i++) {
        std::cin >> p(k - 1, k - 1 - i);
    }
    for (std::size_t i = 0; i < k - 1; i++) {
        p(i, i + 1) = 0xFFFFFFFF;
    }
    M b = p.pow(m - 1) * a;
    std::cout << b(0, 0) << std::endl;
    return 0;
}