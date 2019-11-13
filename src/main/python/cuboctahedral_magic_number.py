import matplotlib.pyplot as plt

MAX_K = 51


def calc_magic_number(K):
    M = (10 * pow(K, 3) + 15 * pow(K, 2) + 11 * K + 3) / 3
    return M


def calc_surface_atoms_count(K):
    N = (10 * pow(K, 2) + 2)
    return N


def plot_magic_number_graph():
    K = list(range(1, MAX_K))
    M = list()
    N = list()
    percent_surface = list()
    percent_bulk = list()

    for i in K:
        m = calc_magic_number(i)
        n = calc_surface_atoms_count(i)
        M.append(m)
        N.append(n)
        percent_surface.append(float(n * 100.0 / (1.0 * m)))
        percent_bulk.append(float((m - n) * 100.0 / (1.0 * m)))

    plt.scatter(K, M, label = 'Total Number of Atoms (M,K)')
    plt.scatter(K, N, label = 'Surface Atoms (N,K)')
    plt.legend(loc = 'best')
    plt.xlabel('K (Number of shells)')
    plt.ylabel('Number of atoms')
    plt.title('Total and Surface Atoms Count Plot!')
    plt.grid()
    plt.show()

    plt.scatter(K, percent_surface, label = '% Surface')
    plt.scatter(K, percent_bulk, label = '% Bulk')
    plt.legend(loc = 'best')
    plt.title('% Surface/Bulk Atoms Plot!')
    plt.xlabel('K (Number of shells)')
    plt.ylabel('% Surface/Bulk atoms')
    plt.grid()
    plt.show()


def main():
    print('Welcome!')
    K = int(input('Enter value of K to get the magic number: '))
    if K >= 1:
        M = int(calc_magic_number(K))
        N = int(calc_surface_atoms_count(K))
        print('Magic Number of Atoms = ', M)
        print('Surface Atoms = ', N)
    else:
        print('Error! Please enter a positive integer value.')

    plot_magic_number_graph()


if __name__ == '__main__':
    main()
