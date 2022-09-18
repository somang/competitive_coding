def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N, R, C, Sr, Sc = map(int, input().split())
        instructions = input()
        final_r, final_c = end_position(N, R, C, Sr, Sc, instructions)
        print(f'Case #{test_case}: {final_r} {final_c}')

# def end_position(N, R, C, Sr, Sc, instructions):
#     visited={}    
#     for i in instructions:
#         visited[(Sr, Sc)] = 1
#         while (Sr, Sc) in visited:
#             move={"E":(Sr, Sc+1), "W":(Sr, Sc-1), "N":(Sr-1, Sc), "S":(Sr+1, Sc)}
#             (Sr, Sc) = move[i]
#     return Sr, Sc


def end_position(N, R, C, Sr, Sc, instructions):
    # TODO: Complete this function and return the 
    #final position (row, column) of the robot
    visited_row, visited_col = {}, {}

    for i in range(1, C+1):
        visited_row[i] = [0, 0]
    for i in range(1, R+1):
        visited_col[i] = [0, 0]
    
    visited_row[Sc] = [Sr, Sr]
    visited_col[Sr] = [Sc, Sc]

    final_r, final_c = 0, 0
    r, c = Sr, Sc
    for i in instructions:
        
        print(f"{r,c} -> {i}")
        if i=="S":
            r += 1
            if r <= visited_row[c][1] and visited_row[c][1] > 0:
                r = visited_row[c][1]+1
            visited_row[c][1] = r            
        elif i=="N":
            r -= 1
            if r >= visited_row[c][0] and visited_row[c][0] > 0:
                r = visited_row[c][0]-1
            visited_row[c][0] = r
        elif i=="E":
            c += 1
            if c <= visited_col[r][1] and visited_col[r][1] > 0:
                c = visited_col[r][1]+1
            visited_col[r][1] = c
        elif i=="W":
            c -= 1
            if c >= visited_col[r][0] and visited_col[r][0] > 0:
                c = visited_col[r][0]-1
            visited_col[r][0] = c
        print(f"{r,c}")
        print(visited_col)
        print(visited_row)
    final_r, final_c = r, c
    return final_r, final_c


if __name__ == '__main__':
    main()
