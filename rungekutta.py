def trajectory(ic, start=0, end=1000, num_samples=176, separation=5, tofile=0):
    xlist, ylist, zlist = [], [], []
    sigma = 10
    rho = 28
    beta = 2 #8/3, but in the original code, integer division floored the answer to 2
    step = 0.01

    x = ic[0]
    y = ic[1]
    z = ic[2]

    j = 0
    for i in range(end):
        k1x = step*funcx(x, y, sigma)
        k1y = step*funcy(x, y, z, rho)
        k1z = step*funcz(x, y, z, beta)

        k2x = step*funcx(x+k1x/2.0, y+k1y/2.0, sigma) #for correct rounding, make sure division is decimal (and not integer) division
        k2y = step*funcy(x+k1x/2.0, y+k1y/2.0, z+k1z/2.0, rho)
        k2z = step*funcz(x+k1x/2.0, y+k1y/2.0, z+k1z/2.0, beta)

        k3x = step*funcx(x+k2x/2.0, y+k2y/2.0, sigma)
        k3y = step*funcy(x+k2x/2.0, y+k2y/2.0, z+k2z/2.0, rho)
        k3z = step*funcz(x+k2x/2.0, y+k2y/2.0, z+k2z/2.0, beta)

        k4x = step*funcx(x+k3x/2.0, y+k3y/2.0, sigma)
        k4y = step*funcy(x+k3x/2.0, y+k3y/2.0, z+k3z/2.0, rho)
        k4z = step*funcz(x+k3x/2.0, y+k3y/2.0, z+k3z/2.0, beta)

        if j < num_samples and start == i:
            xlist.append(round(x,2))
            ylist.append(round(y,2))
            zlist.append(round(z,2))
            j += 1
            start = start+separation

        x = x + (k1x + 2*k2x + 2*k3x + k4x)/6.0
        y = y + (k1y + 2*k2y + 2*k3y + k4y)/6.0
        z = z + (k1z + 2*k2z + 2*k3z + k4z)/6.0

    if tofile == True:
        outfile = open("rungekutta.txt", "w")
        outfile.write("-----4th Order Runge-Kutta Trajectory-----\n")
        outfile.write("IC: (%.3f, %.3f, %.3f)\n" % (ic[0], ic[1], ic[2]))
        outfile.write("Step size: %f\n" % step)
        outfile.write("Values calculated: %d\n" % end)
        outfile.write("Sample interval: %d\n" % separation)
        outfile.write("Total number of samples used: %d\n" % num_samples)
        outfile.write("Rounding all output to 2 decimal places.\n\n")

        outfile.write("i".ljust(6) + "x".ljust(6) + "\n")
        index = 1
        for x in xlist:
            outfile.write(str(index).ljust(6) + str(x).ljust(6) + "\n")
            index += 1
        outfile.close()

    return xlist

def funcx(x, y, sigma):
    return sigma*(y-x)

def funcy(x, y, z, rho):
    return rho*x - y - x*z

def funcz(x, y, z, beta):
    return x*y-beta*z
