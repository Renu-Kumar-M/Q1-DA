pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',url: 'https://github.com/Renu-Kumar-M/Q1-DA.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install -r requirement.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'py -m pytest -q'
            }}}}