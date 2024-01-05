# Huawei Smart Logger 3000 Data Retrieval

This project queries data from a locally owned and operated Huawei Smart Logger 3000 used as part of the Huawei Fusion Solar system and outputs that data as a JSON KVP.

More information can be found [here](https://support.huawei.com/enterprise/en/doc/EDOC1100108365) and [here](https://support.huawei.com/enterprise/en/doc/EDOC1100108365/1a9e42de/webui-layout)

Example usage

```
from huawei_smart_logger import HuaweiSmartLogger3000API
import json
import asyncio

class Test():
    async def main(self):
        hsl = HuaweiSmartLogger3000API("admin","password","192.168.x.x")
        await hsl.fetch_data()
        data_dict = hsl.get_results()
        json_object = json.dumps(data_dict)
        print(json_object)

test=Test()
asyncio.run(test.main())

```
