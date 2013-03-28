import scipy.stats as stats
import matplotlib.pyplot as plot
import matplotlib.mlab as mlab

class ML(object):
    def visualise(self, actual, classified):
        (correlation, unknown) = self.correlation(classified, actual)
        print '{0}\t{1}'.format(correlation, unknown)

        plot.figure(2)
        plot.plot(actual, classified, 'x')
        plot.xlabel('Actual Year')
        plot.ylabel('Classified Year')
#        plot.show()

        actual = [int(a) for a in actual]
        classified = [int(c) for c in classified]

        years_out = [classified_y - actual_y for (classified_y, actual_y) in zip(actual, classified)]

        fig = plot.figure(3)
        ax = fig.add_subplot(111)
        n, bins, patches = ax.hist(years_out, max(max(actual),max(classified)) - min(min(actual),min(classified)))
        m_x = max(abs(min(years_out)),(abs(max(years_out))))

        ax.set_xlim(-m_x, m_x)
        plot.xlabel('Years out')
        plot.ylabel('Number of Paintings')
#        plot.show()

    def correlation(self, classified, actual):
        a = [float(x) for x in classified]
        b = [float(x) for x in actual]
        return stats.pearsonr(a, b)
