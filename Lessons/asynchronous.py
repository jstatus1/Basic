import asyncio

async def find_divisibles(inrange, div_by):
	print("finding nums in range {} divisible by {}". format(inrange, div_by))
	located = []
	for i in range(inrange):
		if i % div_by == 0:
			located.append(i)
	print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
	return located



async def main():
	divs1 = loop.create_task(find_divisibles(508000, 34113))
	divs2 = loop.create_task(find_divisibles(100052, 3210))
	divs3 = loop.create_task(find_divisibles(500, 3))

if __name__ == "__main__":
	try:
		loop = asyncio.get_event_loop()
		loop.run_unit_complete(main())
	except Exception as e:
		pass
	finally:

		loop.close()