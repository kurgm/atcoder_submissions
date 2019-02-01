#include <complex>
#include <iostream>
#include <vector>

using namespace std;

static bool crosses(complex<double> a, complex<double> b, complex<double> c,
                    complex<double> d) {
    complex<double> d2 = (d - a) / (b - a);
    complex<double> c2 = (c - a) / (b - a);
    if (d2.imag() * c2.imag() > 0) {
        return false;
    }
    double r = (c2.imag() * d2.real() - d2.imag() * c2.real()) /
               (c2.imag() - d2.imag());
    return 0.0 < r && r < 1.0;
}

int main() {
    complex<double> a, b;
    {
        double ax, ay, bx, by;
        cin >> ax >> ay >> bx >> by;
        a = complex<double>(ax, ay);
        b = complex<double>(bx, by);
    }
    int n;
    cin >> n;
    vector<complex<double> > coords(n);
    for (int i = 0; i < n; i++) {
        double x, y;
        cin >> x >> y;
        coords[i] = complex<double>(x, y);
    }
    int cnt = 0;
    for (int i = 1; i < n; i++) {
        if (crosses(a, b, coords[i - 1], coords[i])) {
            cnt++;
        }
    }
    if (crosses(a, b, coords[n - 1], coords[0])) {
        cnt++;
    }
    cout << (cnt / 2 + 1) << endl;
    return 0;
}
