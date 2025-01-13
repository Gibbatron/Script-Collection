#!/bin/bash

#############
#run rnaseq pipeline
nextflow run nf-core/rnaseq -profile singularity -c resources/my.config -params-file resources/rnaseq-params.yaml
#############