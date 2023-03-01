# bug reproduction code of roslibpy

- build
```
docker-compose -f docker-compose-ng.yaml build
```
- run test (fail case)
  - use Topic instance both for publish/subscribe
```
docker-compose -f docker-compose-ng.yaml up
```
- run test (work around)
  - use separate Topic instances for publish/subscribe
```
docker-compose -f docker-compose-ok.yaml up
```
