pipeline{
    agent any
    environment{
        PATH = "/hot/new/bin:${env.PATH}"
    //     PATH＋EXTRA = "/path/to/dir:${env.PATH}"
    //     PATH ="/a/new/bin:${env.SCM_HOME}:$PATH"
    }
    stages{
        stage('Gitクローン'){
            steps{
                echo 'Hello World.'
                deleteDir()
                git url: 'https://github.com/Kotaro-Bannai/Sample.git', branch: 'main'
            }
        }
        stage('スクリプト実行'){
            steps{
                echo 'Hello World.'
                // print "WORKSPACE: ${env.WORKSPACE}"
                // sh "export PATH=/usr/local/bin:$PATH"
                echo "PATH is: ${env.PATH}"
                echo "PATH is: ${PATH}"
                sh "sh ./sample.sh >& log"
            }
        }
    }
}
