#!/usr/bin/perl
#
# SLRUM health check suite
# Ulf.Tigerstedt@csc.fi 2012
use strict;
use warnings;
use Filesys::Df;

my $ref = df("/tmp");
if (defined($ref)) {
	if ( $ref->{bfree} < 200*1024 ) {
		exit 1;
	}
}
exit 0;

