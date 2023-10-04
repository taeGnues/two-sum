from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}  # 각 숫자의 인덱스를 저장할 딕셔너리를 생성

    for i, num in enumerate(nums): # i는 번째, num은 nums에 해당하는 값
        complement = target - num
        if complement in num_dict:  # 해당 값이 dic에 있는지 확인.
            return [num_dict[complement], i]  # 숫자 쌍을 찾으면 해당 인덱스를 반환
        num_dict[num] = i

