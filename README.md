vcf-toolbox
===========

A package for graphing, QC, and comparing variant data from VCF files. Uses bcftools.

### Planned Options

	Usage:
	  tb.py listvars <vcf>          
	  tb.py plot <vcf> <x> [<y>]      [options]               
	  tb.py concordance <vcf> [--vcf2=<vcf2>] [--x=<x>] [--values=<values>] [--pairs=<pairset>] 
	  tb.py tstv <vcf> [--x=<x>]
	  tb.py -h | --help
	  tb.py --version

	Options:
	  -h --help                   Show this screen.
	  --version                   Show version.
	  --title=<title>             Set Custom plot titles.
	  --region=<region>           Restrict analysis to a particular region.
	  --include=<filter-expr>     Use a custom filtering string with bcftools.
	  --facet=<facet-var>         Facet analysis on a categorical variable.
	  --split-sample              When plotting genotype FORMAT fields, facet by sample.

## Version 1.0 To Do List

#### General

- [X] List available variables (INFO/General)
- [X] Create/manage files within a created directory [create folder for vcf]
- [X] Create single script for generating plots; append to it date/time, plot title, etc.

#### Common Options

- [X] __--title__ - Set plot options.
- [X] __--logx__ - Put x variable on log scale. (prepend log:)
- [X] __--logy__ - Put y variable on log scale. (prepend log:)
- [ ] __--knitr__ - Create a knitr report; generate option.
- [X] __--include__ - Use a custom filter.
- [X] __--region__ - Restrict analysis to a particular region
- [ ] __--samples__ - Restrict analysis to particular sample(s)
- [ ] __--facet__ - Facet by filter or categorical variable.
- [ ] __--noplot__ - Ignore plotting, but produce plot code.

#### Listing Variables

	tb.py listvars <vcf>

Lists variables available for use in plotting within a vcf file. Outputs tables that look like this:

FORMAT FIELDS

+-----------+--------------------------------------------------+---------+
| id        | desc                                             | type    |
+===========+==================================================+=========+
| FORMAT/GT | Genotype                                         | String  |
+-----------+--------------------------------------------------+---------+
| FORMAT/GQ | Genotype Quality                                 | Integer |
+-----------+--------------------------------------------------+---------+
| FORMAT/SP | Phred-scaled strand bias P-value                 | Integer |
+-----------+--------------------------------------------------+---------+
| FORMAT/PL | List of Phred-scaled genotype likelihoods        | Integer |
+-----------+--------------------------------------------------+---------+
| FORMAT/DV | # high-quality non-reference bases               | Integer |
+-----------+--------------------------------------------------+---------+
| FORMAT/GL | Likelihoods for RR,RA,AA genotypes (R=ref,A=alt) | Float   |
+-----------+--------------------------------------------------+---------+
| FORMAT/DP | # high-quality bases                             | Integer |
+-----------+--------------------------------------------------+---------+

#### Plotting Variables

	tb.py plot <vcf> <x> [<y>]

- [ ] plot individual variable
	- [X] Numeric
	- [X] String
    - [X] plot variant density across genome
		- [X] Genetic Labels (Mb, Kb, etc; Commas)
		- [X] bin-width
	- [ ] Multi-value fields
		- [ ] Reshaping
	- [ ] Options
- [ ] Plot multiple variables
	- [ ] Numeric x String
	- [ ] Numeric x Numeric (Scatterplot)
		- [ ] Labels (e.g. color by filter, another variable, tstv ratio)
	- [ ] Multi-value fields.
	- [ ] Plot along chromosomal coordinates (e.g. DP by CHROM:POS)
	- [ ] Options


#### Concordance Analysis

	tb.py concordance <vcf>

- [X] Single Variable x Rate of Discordance (data is produced)
- [X] Marking Pairs
- [ ] Allow specifying specific values and ranges as comma delimited list (--values option).
- [ ] Dealing with 2 files (merging, etc.)
- [ ] Parallelize to speed up.
- [ ] Plots
	- [ ] Heatmap (when run without variable)
	- [ ] Split when there are a large number of samples into smaller heatmaps.
	- [ ] Concordance  across variable.
- [X] Binning for many observations.
- [X] Statify by variable.

#### tstv analysis

	tb.py tstv <vcf> --x=<x>

Output a report on tstv or examine tstv across a given variable.

- [X] Stratify tstv across variable
- [X] ts/tv ratio by chromosome:position; summary table
- [ ] Use bcftools to calculate ts and tv when not stratifying by variable (speed up)
- [X] Plots
	- [X] plot aggregate (all)
	- [X] plot categorical (by sample)
	- [X] plot numeric (by sample) and aggregate

#### Quality Control

	tb.py QC <vcflist>...

Outputs a QC report of one or more vcfs. If two vcfs are given, will compare them (and take considerably longer to run).

#### Special

Odds and Ends

- [ ] Allele frequency spectrum
- [ ] Base Changes (Frequency)
- [ ] Insertion/Deletion Lengths
	
#### Future

* Plot on z axis?
* Multiple vcf comparison (Merge first?)
* Bokeh?
