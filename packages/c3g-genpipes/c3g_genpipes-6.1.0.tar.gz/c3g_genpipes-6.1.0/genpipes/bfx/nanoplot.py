################################################################################
# Copyright (C) 2025 C3G, The Victor Phillip Dahdaleh Institute of Genomic Medicine at McGill University
#
# This file is part of GenPipes.
#
# GenPipes is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GenPipes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with GenPipes.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import os

# MUGQIC Modules
from ..core.config import global_conf
from ..core.job import Job


def qc(
    output_dir,
    output_prefix,
    input_bam=None,
    input_fastq=None,
    input_summary=None,
    aligned = False,
    is_directory = False,
    ini_section='nanoplot'
    ):
    """
    QC metrics with NanoPlot.

    :return: a job for NanoPlot QC
    """

    output = [
        os.path.join(output_dir, output_prefix + "NanoPlot-report.html"),
        os.path.join(output_dir, output_prefix + "NanoStats.txt")
    ]

    if is_directory and input_fastq:
        fastq_input = f"{input_fastq}/*"
    elif input_fastq:
        fastq_input = input_fastq
    else:
        fastq_input = None

    bam_flag = "--ubam " if aligned==False else "--bam "

    return Job(
        [input_bam, input_fastq],
        output,
        [
            [ini_section, "module_nanoplot"]
        ],
        command="""\
NanoPlot {other_options} \\
  {input_bam} {input_fastq} {input_summary} \\
  -o {output_dir} \\
  -p {output_prefix} \\
  --threads {threads}""".format(
            other_options=global_conf.global_get(ini_section, 'other_options', required=False),
            input_bam=bam_flag + input_bam if input_bam else "",
            input_fastq="--fastq " + fastq_input if input_fastq else "",
            input_summary="--summary " + input_summary if input_summary else "",
            threads=global_conf.global_get(ini_section, 'threads'),
            output_dir=output_dir,
            output_prefix=output_prefix
        )
    )
