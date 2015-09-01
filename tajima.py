#! /usr/bin/env python
"""
usage:
  tb.py tajima 

Example

command:
  tajima        Calculate Tajima's D

options:
  -h --help                   Show this screen.
  --version                   Show version.



"""
from docopt import docopt
from subprocess import call
from itertools import combinations
from utils.vcf import *
from math import isinf
import sys



debug = None
if len(sys.argv) == 1:
    debug = ['tajima']



class tajima(vcf):
    """
      Subclass of the vcf object
      used for calculating tajima's D
    """
    def __init__(self, filename):
      vcf.__init__(self,filename)

    def calc_tajima(self):
        # Tajima D Constants
        n = self.n*2
        a1 = sum([1.0/i for i in xrange(1,n)])
        a2 = sum([1.0/i**2 for i in xrange(1,n)])
        b1 = (n + 1.0) / (3.0*(n - 1))
        b2 = (2.0 * (n**2 + n + 3.0)) / \
           (9.0 * n * (n -1.0))
        c1 = b1 - (1.0 / a1)
        c2 = b2 - ((n + 2.0) / (a1*n)) + (a2 / (a1**2) )
        e1 = c1 / a1
        e2 = c2 / (a1**2 + a2)

        for variant_interval in self.window(window_size=100000, shift_method="POS-Interval"):
            pi = 0.0
            n_sites = 0
            gt = np.vstack([x.gt_types for x in variant_interval])
            S = 0
            for variant in variant_interval:
                AN = variant.INFO.get("AN")  # c;AN : total number of alleles in called genotypes
                AC = variant.INFO.get("AC")  # j;AC : allele count in genotypes, for each ALT allele, in the same order as listed
                try:
                    # Biallelic sites only!
                    pi += (2.0 * AC * (AN-AC)) / (AN * (AN-1.0))
                    S += 1
                except:
                    pass
            try:
                CHROM = variant_interval[0].CHROM
                tw = (S / a1)
                var = (e1 * S) + ((e2 * S) * (S - 1.0))
                TajimaD = (pi - tw) / \
                          (var)**(0.5)
                if not isinf(TajimaD) and S > 0:
                    yield CHROM, variant_interval.lower_bound, variant_interval.upper_bound, n_sites, TajimaD
            except:
                pass


class variant_ops:
    """
        Variant operator - takes a variant interval as input
        and enables certain operations to be performed
    """
    def __init__(self, variant_interval, vcf):
        # self.shift_method = shift_method
        self.interval = variant_interval.interval()
        self.gt = np.vstack([x.gt_types for x in variant_interval])
        self.n = vcf.n 
        self.segregating_sites = sum([np.any(p) for p in np.equal(3, self.gt)])
        #print self.gt.T
        #print np.vstack([x.gt_bases for x in variant_interval]).T
        print self.segregating_sites
        self.a1 = H(self.n) # Number of DNA sequences



if __name__ == '__main__':
    args = docopt(__doc__, 
                  version='VCF-Toolbox v0.1',
                  argv = debug,
                  options_first=True)
    print(args)
    print "TAJIMA"


v = tajima("/Users/dancook/coding/git/vcf-toolbox/test.vcf.gz")
print dir(v)
for i in v.calc_tajima():
    print "\t".join([str(x) for x in i])
    

