UPDATE salary SET 
    sex = CASE sex WHEN 'm' THEN 'f' ELSE 'm' END;


-- Runtime: 290 ms, faster than 17.32% of MySQL online submissions for Swap Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.