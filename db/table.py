#!/bin/env python

import sys;

sql='''drop table if exists `ipad_hk`;

CREATE TABLE `ipad_hk` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `data` varchar(1024000) DEFAULT NULL,
    `status` int(11) DEFAULT 0,
    `updatetime` datetime,
	`comment` varchar(64) DEFAULT NULL,
    PRIMARY KEY (`id`),
	KEY `status_idx` (`status`),
	KEY `updatetime_idx` (`updatetime`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
'''

sql = sql.replace("ipad_hk", sys.argv[1])

print sql
