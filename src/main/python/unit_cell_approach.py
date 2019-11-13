import matplotlib.pyplot as plt

MAX_N = 51


def calc_magic_number(N):
    total_atoms_count = (4 * pow(N, 3) + 6 * pow(N, 2) + 3 * N + 1)
    return total_atoms_count


def calc_surface_atoms_count(N):
    surface_atoms_count = (12 * pow(N, 2) + 2)
    return surface_atoms_count


def plot_magic_number_graph():
    N = list(range(1, MAX_N))
    total_atoms_count = list()
    surface_atoms_count = list()
    percent_surface = list()
    percent_bulk = list()

    for i in N:
        m = calc_magic_number(i)
        n = calc_surface_atoms_count(i)
        total_atoms_count.append(m)
        surface_atoms_count.append(n)
        percent_surface.append(float(n * 100.0 / (1.0 * m)))
        percent_bulk.append(float((m - n) * 100.0 / (1.0 * m)))

    plt.scatter(N, total_atoms_count, label = 'Total Number of Atoms')
    plt.scatter(N, surface_atoms_count, label = 'Number of Surface Atoms')
    plt.legend()
    plt.xlabel('N (Number of Unit Cells)')
    plt.ylabel('Number of atoms')
    plt.title('Total and Surface Atoms Count Plot! (for FCC)')
    plt.grid()
    plt.show()

    plt.scatter(N, percent_surface, label = '% Surface')
    plt.scatter(N, percent_bulk, label = '% Bulk')
    plt.legend()
    plt.title('% Surface/Bulk Atoms Plot! (for FCC)')
    plt.xlabel('Particle Size')
    plt.ylabel('% Surface/Bulk atoms')
    plt.grid()
    plt.show()


def main():
    print('Welcome!')
    K = int(input('Enter value of N to get the results: '))
    if K >= 1:
        M = int(calc_magic_number(K))
        N = int(calc_surface_atoms_count(K))
        print('Total Number of Atoms = ', M)
        print('Surface Atoms = ', N)
    else:
        print('Error! Please enter a positive integer value.')

    plot_magic_number_graph()


if __name__ == '__main__':
    main()
