import matplotlib.pyplot as plt

MAX_A = 51


def surface_to_vol_ratio(a, shape):
    if shape == 'slab':
        return float(2.0 / a)
    elif shape == 'cylinder':
        return float(2.0 / a)
    elif shape == 'cube':
        return float(6.0 / a)
    elif shape == 'sphere':
        return float(3.0 / a)


def main():
    a = list()
    surface_to_vol_ratio_slab = list()
    surface_to_vol_ratio_cylinder = list()
    surface_to_vol_ratio_cube = list()
    surface_to_vol_ratio_sphere = list()

    for i in range(1, MAX_A):
        sub_div = [0.0, 0.25, 0.50, 0.75]
        for j in sub_div:
            a.append(i + j)
            surface_to_vol_ratio_slab.append(surface_to_vol_ratio(i + j, 'slab'))
            surface_to_vol_ratio_cylinder.append(surface_to_vol_ratio(i + j, 'cylinder'))
            surface_to_vol_ratio_cube.append(surface_to_vol_ratio(i + j, 'cube'))
            surface_to_vol_ratio_sphere.append(surface_to_vol_ratio(i + j, 'sphere'))

    plt.plot(a, surface_to_vol_ratio_cylinder, label = 'Cylinder')
    plt.plot(a, surface_to_vol_ratio_cube, label = 'Cube')
    plt.plot(a, surface_to_vol_ratio_sphere, label = 'Sphere')

    plt.title('Surface to Volume Ratio Plot!')
    plt.xlabel('Critical Dimension (nm)')
    plt.ylabel('Surface to Volume Ratio (1/nm)')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
