#!/usr/bin/perl
use File::Basename;
use lib dirname(__FILE__);
use country_codes;
use strict;
use Data::Dumper;

#Read in the first ten lines of the file
my @list_from_file = `tail /share/logs/noaa-web/download.log`;

my @datasets = ('G02135', 'nsidc-0008', 'nsidc-0057', 'G00788', 'G00799');
my %dataset_sizes;
my %dataset_downloads;
my %unique_users;
my %ip_info;
my %domain_info;

my $total_size = 0;
my $total_downloads = 0;

my %country_codes = %country_codes::COUNTRY_CODES;

#Iterate over the lines from the list
foreach my $line_from_file (@list_from_file) {
        #Run our regular expression to parse out fields based on whitespace.
        my @fields_from_line = $line_from_file =~ /(\S+)\s+/g;

        foreach my $dataset (@datasets) {
                if ($fields_from_line[5] =~ /$dataset/) {
                        $dataset_sizes{$dataset} += $fields_from_line[4];
                        $dataset_downloads{$dataset}++;

                        #set this hash map keys to the IP address.
                        $unique_users{$dataset}{$fields_from_line[3]} = 1;
                }
        }

        $total_size += $fields_from_line[4];
        $total_downloads++;

        if (! exists $ip_info{$fields_from_line[3]}) {
          $ip_info{$fields_from_line[3]} = join("", `nslookup $fields_from_line[3]`);
          $ip_info{$fields_from_line[3]} =~ s/\s//sg;
        }
        (my $country_code) = $ip_info{$fields_from_line[3]} =~ /\.([^\.]+)\.$/s;
        $domain_info{$country_codes{$country_code}}{users}{$fields_from_line[3]} = 1;
        $domain_info{$country_codes{$country_code}}{downloads}++;
        $domain_info{$country_codes{$country_code}}{volume}+= $fields_from_line[4];
}


print "Transfers by Data Set\n";
print "--------------------------------------------------\n";
print "Dataset, Distinct Users, # of Files, Volume (MB) \n";
print "--------------------------------------------------\n";
foreach my $dataset (@datasets) {
        print "$dataset,    ", scalar(keys %{$unique_users{$dataset}}),", $dataset_downloads{$dataset}, $dataset_sizes{$dataset}\n";
}
print "\n";
foreach my $country_code (keys %domain_info) {
  print "$country_code, ", scalar(keys %{$domain_info{$country_code}{users}}), "\n"; 
}
print "\n";
print "total size $total_size\n";
print "total downloads $total_downloads\n";
