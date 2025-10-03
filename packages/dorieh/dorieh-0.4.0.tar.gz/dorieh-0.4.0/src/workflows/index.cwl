#!/usr/bin/env cwl-runner
### Index Builder
#  Copyright (c) 2021. Harvard University
#
#  Developed by Research Software Engineering,
#  Faculty of Arts and Sciences, Research Computing (FAS RC)
#  Author: Michael A Bouzinier
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

cwlVersion: v1.2
class: CommandLineTool
baseCommand: [python, -m, dorieh.platform.loader.index_builder]
requirements:
  InlineJavascriptRequirement: {}
  NetworkAccess:
    networkAccess: True

doc: |
  This tool builds all indices for the specified table.
  Log file displays real-time progress of building indices



hints:
  DockerRequirement:
    dockerPull: forome/dorieh

inputs:
  #$import: db.yaml
  registry:
    type:
      - File?
      - string?
    inputBinding:
      prefix: --registry
    doc: |
      A path to the data model file
  domain:
    type: string
    doc: the name of the domain
    inputBinding:
      prefix: --domain
  table:
    type: string
    doc: the name of the table
    inputBinding:
      prefix: --table
  database:
    type: File
    doc: Path to database connection file, usually database.ini
    inputBinding:
      prefix: --db
  connection_name:
    type: string
    doc: The name of the section in the database.ini file
    inputBinding:
      prefix: --connection
  incremental:
    type:  boolean
    default: false
    inputBinding:
      prefix: --incremental
  force:
    type:  boolean
    default: false
    inputBinding:
      prefix: --force
  depends_on:
    type: Any?
    doc: a special field used to enforce dependencies and execution order


arguments:
    - valueFrom: "--autocommit"


outputs:
  log:
    type: File
    outputBinding:
      glob: "*.log"
  errors:
    type: stderr

stderr:  $("index-" + inputs.table + ".err")

