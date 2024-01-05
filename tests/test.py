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


