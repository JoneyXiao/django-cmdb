**NI = Not Implemented and will return a 405 METHOD NOT ALLOWED response**

| URI | GET | PUT | POST | DELETE |
|:----|:----|:----|:-----|:-------|
| /Containers | Returns a list of all Device Classes | NI  | NI   | NI     |
| /Random/CMDB/Path | Returns list of all objects in this device class,or the single object if there is only one | Updates the CMDB object | Adds a new device in this class if POSTing to a container| Delete (actually decommission) the object, not valid if done on a container |