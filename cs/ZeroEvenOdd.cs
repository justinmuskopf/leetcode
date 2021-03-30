using System.Threading;

public class ZeroEvenOdd {
    private int n;

    // 0: Zero, Odd is next
    // 1: Odd, Zero is next
    // 2: Zero, Even is next
    // 3: Even, Zero is next (set to 0)
    private int state = 0;
    
    readonly object _lock = new object();
    
    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Zero(Action<int> printNumber) {
        // There will be n zeroes
        for (int i = 0; i < n; i++) {
            lock (_lock) {
                while (state != 0 && state != 2) {
                    Monitor.Wait(_lock);
                }

                printNumber(0);
                state++;

                Monitor.PulseAll(_lock);
            }
        }
    }

    public void Even(Action<int> printNumber) {
        // There will be n/2 even numbers
        for (int i = 2; i <= n; i += 2) {
            lock (_lock) {
                while (state != 3) {
                    Monitor.Wait(_lock);
                }

                printNumber(i);
                state = 0;

                Monitor.PulseAll(_lock);
            }
        }
    }

    public void Odd(Action<int> printNumber) {
        // There will be n/2 odd numbers
        for (int i = 1; i <= n; i += 2) {
            lock (_lock) {
                while (state != 1) {
                    Monitor.Wait(_lock);
                }

                printNumber(i);
                state = 2;

                Monitor.PulseAll(_lock);
            }
        }
    }
}