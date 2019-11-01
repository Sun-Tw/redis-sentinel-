安装与配置 redis哨兵模式
redis-sentinel

```
1.配置开启主从节点
2.配置开启sentinel监控主节点。(sentinel是特殊的redis)
3.实际应该多台机器
4.详细配置节点

最终目标
master-7000  slave-7001 slave-7002
sentinel-26379 sentinel-26380 sentinel-26381
```



```
redis-server redis-7000.conf
redis-server redis-7001.conf
redis-server redis-7002.conf

redis-sentinel redis-sentinel-26379.conf
redis-sentinel redis-sentinel-26380.conf
redis-sentinel redis-sentinel-26381.conf
```



