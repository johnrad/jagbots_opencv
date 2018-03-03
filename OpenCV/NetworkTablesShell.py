Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import networktables
>>> from networktables import NetworkTables
>>> NetworkTables.initialize(server='10.46.38.2')
False
>>> table = NetworkTables.getDefault()
>>> table
<networktables.instance.NetworkTablesInstance object at 0x05898470>
>>> read error: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
KeyboardInterrupt
>>> from networktables import NetworkTables
>>> NetworkTables.initialize(server='10.46.38.2')
False
>>> table = NetworkTables.getDefault()
>>> table
<networktables.instance.NetworkTablesInstance object at 0x05898470>
>>> table.getEntry('CameraPublisher/Cube/streams')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    table.getEntry('CameraPublisher/Cube/streams')
  File "C:\Users\james\AppData\Local\Programs\Python\Python36-32\lib\site-packages\networktables\instance.py", line 191, in getEntry
    assert name.startswith('/')
AssertionError
>>> table.getEntry('/CameraPublisher/Cube/streams')
<NetworkTableEntry: Value(type=b'@', value=('mjpg:http://roborio-4638-frc:1181/stream.mjpg?name=Cube', 'mjpg:http://10.46.38.2:1181/stream.mjpg?name=Cube'))>
>>> Cube_Stream = table.getEntry('/CameraPublisher/Cube/streams')
>>> Cube_Stream
<NetworkTableEntry: Value(type=b'@', value=('mjpg:http://roborio-4638-frc:1181/stream.mjpg?name=Cube', 'mjpg:http://10.46.38.2:1181/stream.mjpg?name=Cube'))>
>>> NetworkTables.putString('/test','Mad Hacks Bro')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    NetworkTables.putString('/test','Mad Hacks Bro')
AttributeError: 'NetworkTablesInstance' object has no attribute 'putString'
>>> table.putString('/test','Mad Hacks Bro')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    table.putString('/test','Mad Hacks Bro')
AttributeError: 'NetworkTablesInstance' object has no attribute 'putString'
>>> table.putString('/test','Mad Hacks Bro')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    table.putString('/test','Mad Hacks Bro')
AttributeError: 'NetworkTablesInstance' object has no attribute 'putString'
>>> tableroot = table.getEntry('/')
>>> tableroot.putString('test','whatever')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tableroot.putString('test','whatever')
AttributeError: 'NetworkTableEntry' object has no attribute 'putString'
>>> tableroot.putNumber(1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tableroot.putNumber(1)
AttributeError: 'NetworkTableEntry' object has no attribute 'putNumber'
>>> table.putNumber('number',5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    table.putNumber('number',5)
AttributeError: 'NetworkTablesInstance' object has no attribute 'putNumber'
>>> table
<networktables.instance.NetworkTablesInstance object at 0x05898470>
>>> dir(table)
['DEFAULT_PORT', 'EntryFlags', 'EntryTypes', 'NetworkModes', 'NotifyFlags', 'PATH_SEPARATOR', '_NetworkTablesInstance__createEntry', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', '_conn_listeners', '_defaultInstance', '_entry_listeners', '_init', '_ntproperties', '_tables', 'addConnectionListener', 'addEntryListener', 'addEntryListenerEx', 'addGlobalListener', 'addGlobalListenerEx', 'create', 'deleteAllEntries', 'enableVerboseLogging', 'flush', 'getConnections', 'getDefault', 'getEntries', 'getEntry', 'getEntryInfo', 'getGlobalAutoUpdateValue', 'getGlobalTable', 'getNetworkMode', 'getRemoteAddress', 'getTable', 'globalDeleteAll', 'initialize', 'isConnected', 'isServer', 'loadEntries', 'loadPersistent', 'removeConnectionListener', 'removeEntryListener', 'removeGlobalListener', 'saveEntries', 'savePersistent', 'setDashboardMode', 'setNetworkIdentity', 'setServer', 'setServerTeam', 'setUpdateRate', 'shutdown', 'startClient', 'startClientTeam', 'startDSClient', 'startServer', 'startTestMode', 'stopClient', 'stopServer', 'waitForConnectionListenerQueue', 'waitForEntryListenerQueue']
>>> methods = dir(table)
>>> for method in methods:
	print(method)

	
DEFAULT_PORT
EntryFlags
EntryTypes
NetworkModes
NotifyFlags
PATH_SEPARATOR
_NetworkTablesInstance__createEntry
__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
__weakref__
_api
_conn_listeners
_defaultInstance
_entry_listeners
_init
_ntproperties
_tables
addConnectionListener
addEntryListener
addEntryListenerEx
addGlobalListener
addGlobalListenerEx
create
deleteAllEntries
enableVerboseLogging
flush
getConnections
getDefault
getEntries
getEntry
getEntryInfo
getGlobalAutoUpdateValue
getGlobalTable
getNetworkMode
getRemoteAddress
getTable
globalDeleteAll
initialize
isConnected
isServer
loadEntries
loadPersistent
removeConnectionListener
removeEntryListener
removeGlobalListener
saveEntries
savePersistent
setDashboardMode
setNetworkIdentity
setServer
setServerTeam
setUpdateRate
shutdown
startClient
startClientTeam
startDSClient
startServer
startTestMode
stopClient
stopServer
waitForConnectionListenerQueue
waitForEntryListenerQueue
>>> table
<networktables.instance.NetworkTablesInstance object at 0x05898470>
>>> read error: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
dir(pynetworktables)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dir(pynetworktables)
NameError: name 'pynetworktables' is not defined
>>> dir(networktables)
['NetworkTables', 'NetworkTablesInstance', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'entry', 'instance', 'networktables', 'version']
>>> dir(networktables)['version']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dir(networktables)['version']
TypeError: list indices must be integers or slices, not str
>>> networktables['version']
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    networktables['version']
TypeError: 'module' object is not subscriptable
>>> networktables.version
<module 'networktables.version' from 'C:\\Users\\james\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\networktables\\version.py'>
>>> networktables.version()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    networktables.version()
TypeError: 'module' object is not callable
>>> print(networktables.__version__)
2018.0.1
>>> dir(table)
['DEFAULT_PORT', 'EntryFlags', 'EntryTypes', 'NetworkModes', 'NotifyFlags', 'PATH_SEPARATOR', '_NetworkTablesInstance__createEntry', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', '_conn_listeners', '_defaultInstance', '_entry_listeners', '_init', '_ntproperties', '_tables', 'addConnectionListener', 'addEntryListener', 'addEntryListenerEx', 'addGlobalListener', 'addGlobalListenerEx', 'create', 'deleteAllEntries', 'enableVerboseLogging', 'flush', 'getConnections', 'getDefault', 'getEntries', 'getEntry', 'getEntryInfo', 'getGlobalAutoUpdateValue', 'getGlobalTable', 'getNetworkMode', 'getRemoteAddress', 'getTable', 'globalDeleteAll', 'initialize', 'isConnected', 'isServer', 'loadEntries', 'loadPersistent', 'removeConnectionListener', 'removeEntryListener', 'removeGlobalListener', 'saveEntries', 'savePersistent', 'setDashboardMode', 'setNetworkIdentity', 'setServer', 'setServerTeam', 'setUpdateRate', 'shutdown', 'startClient', 'startClientTeam', 'startDSClient', 'startServer', 'startTestMode', 'stopClient', 'stopServer', 'waitForConnectionListenerQueue', 'waitForEntryListenerQueue']
>>> table
<networktables.instance.NetworkTablesInstance object at 0x05898470>
>>> 
>>> table.getEntry('test')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    table.getEntry('test')
  File "C:\Users\james\AppData\Local\Programs\Python\Python36-32\lib\site-packages\networktables\instance.py", line 191, in getEntry
    assert name.startswith('/')
AssertionError
>>> table.getEntry('/test')
<NetworkTableEntry: None>
>>> entry = table.getEntry('/test')
>>> dir(entry)
['_NetworkTableEntry__api', '__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_local_id', '_value', 'addListener', 'clearFlags', 'clearPersistent', 'delete', 'exists', 'forceSetBoolean', 'forceSetBooleanArray', 'forceSetDouble', 'forceSetDoubleArray', 'forceSetNumber', 'forceSetNumberArray', 'forceSetRaw', 'forceSetString', 'forceSetStringArray', 'forceSetValue', 'get', 'getBoolean', 'getBooleanArray', 'getDouble', 'getDoubleArray', 'getFlags', 'getHandle', 'getInfo', 'getName', 'getNumber', 'getRaw', 'getString', 'getStringArray', 'getType', 'isPersistent', 'key', 'removeListener', 'setBoolean', 'setBooleanArray', 'setDefaultBoolean', 'setDefaultBooleanArray', 'setDefaultDouble', 'setDefaultDoubleArray', 'setDefaultNumber', 'setDefaultNumberArray', 'setDefaultRaw', 'setDefaultString', 'setDefaultStringArray', 'setDefaultValue', 'setDouble', 'setDoubleArray', 'setFlags', 'setNumber', 'setNumberArray', 'setPersistent', 'setRaw', 'setString', 'setStringArray', 'setValue', 'value']
>>> dir(table)
['DEFAULT_PORT', 'EntryFlags', 'EntryTypes', 'NetworkModes', 'NotifyFlags', 'PATH_SEPARATOR', '_NetworkTablesInstance__createEntry', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', '_conn_listeners', '_defaultInstance', '_entry_listeners', '_init', '_ntproperties', '_tables', 'addConnectionListener', 'addEntryListener', 'addEntryListenerEx', 'addGlobalListener', 'addGlobalListenerEx', 'create', 'deleteAllEntries', 'enableVerboseLogging', 'flush', 'getConnections', 'getDefault', 'getEntries', 'getEntry', 'getEntryInfo', 'getGlobalAutoUpdateValue', 'getGlobalTable', 'getNetworkMode', 'getRemoteAddress', 'getTable', 'globalDeleteAll', 'initialize', 'isConnected', 'isServer', 'loadEntries', 'loadPersistent', 'removeConnectionListener', 'removeEntryListener', 'removeGlobalListener', 'saveEntries', 'savePersistent', 'setDashboardMode', 'setNetworkIdentity', 'setServer', 'setServerTeam', 'setUpdateRate', 'shutdown', 'startClient', 'startClientTeam', 'startDSClient', 'startServer', 'startTestMode', 'stopClient', 'stopServer', 'waitForConnectionListenerQueue', 'waitForEntryListenerQueue']
>>> 
