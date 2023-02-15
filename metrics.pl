#!/usr/bin/perl

#Read in the first ten lines of the file
@list_from_file = `tail download.log`;

@datasets = ('G02135', 'nsidc-0008', 'nsidc-0057', 'G00788');
%dataset_sizes;
%dataset_downloads;
%unique_users;

$total_size = 0;
$total_downloads = 0;

#Iterate over the lines from the list
foreach $line_from_file (@list_from_file) {
        #Run our regular expression to parse out fields based on whitespace.
        @fields_from_line = $line_from_file =~ /(\S+)\s+/g;

        foreach $dataset (@datasets) {
                if ($fields_from_line[5] =~ /$dataset/) {
                        $dataset_sizes{$dataset} += $fields_from_line[4];
                        $dataset_downloads{$dataset}++;

                        #set this hash map keys to the IP address.
                        $unique_users{$dataset}{$fields_from_line[3]} = 1;
                }
        }

        $total_size += $fields_from_line[4];
        $total_downloads++;
}

print "Transfers by Data Set\n";
print "--------------------------------------------------\n";
print "Dataset, Distinct Users, # of Files, Volume (MB) \n";
print "--------------------------------------------------\n";
foreach $dataset (@datasets) {
        print "$dataset, ,$dataset_sizes{$dataset}, $dataset_downloads{$dataset}\n";
}
print keys %unique_users;
print "\n";
print values %unique_users;
print "\n";
print scalar keys %unique_users;
print "\n";
print "total size $total_size\n";
print "total downloads $total_downloads\n";
