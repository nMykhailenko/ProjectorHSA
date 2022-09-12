## Stress testing using Siege
 
 To run this solution you need: 
 1. git clone git@github.com:nMykhailenko/ProjectorHSA.git
 2. cd homework4
 3. cd deployment
 4. docker-compose build
 5. docker-compose up
 6. cd ../tests/stress-tests
 4. docker build -t projector-siege . 
 7. docker run --rm --net deployment_projector-stress-test -t projector-siege -d1 -r10 -c25 -f /app/urls.txt