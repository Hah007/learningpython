from __future__ import print_function
import json

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre+[key, '{}']
                else:
                    for d in dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:                   
                    yield pre+[key, '[]']
                else:
                    for v in range(len(value)):
                        for d in dict_generator(value[v], pre + [key, v]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre+[key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict

if __name__ == "__main__":
    sJOSN = '''
   {
    "detail":{
        "baseline":{
            "cancel_scheduled_task":"1",
            "comeonstage":"topwin",
            "conf_ver":2635792175,
            "conf_ver_s":"f7f8ac46##",
            "mission_id":0,
            "rules":{

            },
            "scheduled_task":"1",
            "scheduled_task_rule":{
                "autoexec_on_coundown":"1",
                "exec_countdown":"0",
                "exec_interval":"0",
                "exec_mode":"4",
                "exec_time":"*|00|*|*|*",
                "extra":{
                    "countdown_type":"3600",
                    "cycle_type":"1",
                    "every_type":"1"
                },
                "gid":0,
                "is_notice":"1",
                "is_reportback":"0",
                "module_id":3,
                "name":"",
                "notice_msg":"",
                "status":1,
                "tpl_id":420,
                "type":1
            }
        }
    },
    "id":1,
    "type":2100
}
 ''' 
    sValue = json.loads(sJOSN)
    for i in dict_generator(sValue):
        # print(i)
        print('.'.join(i[0:-1]), ':', i[-1])
