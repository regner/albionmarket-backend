echo off
kubectl.exe --namespace albionmarket set image deploy/albionmarket-backend albionmarket-backend=us.gcr.io/personal-projects-1369/albionmarket/backend:%1