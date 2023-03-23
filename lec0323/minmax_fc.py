def minmax(nums):
    for n in nums:
        mx = max(nums)
        mn = min(nums)

        return [mn,mx]
        return mn,mx



    pass

def main():
    x = [3,7,25,10,2,13]
    mn=minmax(x)[0]
    mx=minmax(x)[1]
    mn, mx = minmax(x)
    print(f"가장 작은 수는 {mn}이고 가장 큰 수는 {mx}이다.")

if __name__ == "__main__":
    main()