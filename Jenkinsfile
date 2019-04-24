// This file is part of the research.fi API service
//
// Copyright 2019 Ministry of Education and Culture, Finland
//
// :author: CSC - IT Center for Science Ltd., Espoo Finland servicedesk@csc.fi
// :license: MIT
node {
  stage('Print environment variables') {
    echo sh(returnStdout: true, script: 'env')
  }
  
  stage('Clone repository') {
    checkout scm
  }
}