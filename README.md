# Data
## To-Do
- [x] Test sensors
- [ ] Integrate sensors and OBC
- [ ] Improve wind speed measuring
- [ ] Improve Serial comms protocol
### Serial Comms protocol
Example string received from Arduino to OBC
```
12 ## 77 ## 12 ## 21 ## 31 ## 4323 ## 737 ## 
```
Data in order is;
1. Humidity
2. Temperature
3. Heat index
4. Time (anemometer)
5. Wind speed
6. Aceleration (x,y,z)
7. Rotation (x,y,z)
