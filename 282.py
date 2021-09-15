# https://leetcode.com/problems/expression-add-operators/

'''
        # Motivation/Strategy
        We need to find the recurrence between subproblems.      
        
        Lets define terms as follows:
            Define number/NUM as [0-9]
            Define operator/OP as {+, -, *}
            Define expression/EXPR as NUM | EXPR OP NUM
            
        Suppose we are given two expressions and an operator, (expr1, expr2, op).
        How can we combine them? What ancilliary information do we need?
        More specifically, how can we evaluate the following:
        
            expr1 op expr2
        
        There are three cases: addition, multiplication, and subtraction
        
        ## Addition
        In the case of adding expressions together, we have
        
            eval(expr1 + expr2)
            
        Because of precedence rules, we can always perform addition last. It then suffices to compute the following:
        
            eval(expr1 + expr2) -> eval(expr1) + eval(expr2)
        
        ## Subtraction.1
        In the case of subtracting expressions, we have 
        
            eval(expr1 - expr2)
        
        We can rewrite this as the following:
        
            eval(expr1 + (-1)*expr2)
        
        as we can see, we will need multiplication
        
        ## Multiplication
        In the case of multiplication of expressions, we have
        
            eval(expr1 * expr2)
            
        We can try the above as follows
            
            eval(expr1 * expr2) =? eval(expr1) * eval(expr2)

        This may fail due to precedence rules since multiplication occurs first.
        An example of this is as follows:
        
            expr1 = 1+2
            exrp2 = 3+4
            
            eval(1+2 * 3+4)       = 1+6+4 = 11
            eval(1+2) * eval(3+4) = 3*7   = 21
            
        As we can see, this fails due to precedence. It as if 2 and 3 are lost
        to expr1 and expr2 respectively. We can use this observation like the following:
        
            eval(1+2 * 3+4)
            = (eval(1+2)-2) + (2*3) + (-3+eval(3+4))
            = 1 + 6 + 4
            = 11
            
        This is what we are expecting. Thus in order to recur, we need to know what is
        "lost" in expr1 and expr2. What exactly do we lose?
        
        We lose the entire product on the right side of expr1 and likewise for the 
        left side of expr2.
        
        Definitions:
            Define "right multiplication group"/RMG of expression/EXPR
                as "right number of EXPR" | number * RMG
                where "right number of EXPR" is the rightmost number of EXPR
            Define "left multiplication group"/LMG similarly

        A maximal RMG of EXPR is the longest RMG. From now on, we will refer to
        the maximal RMG of EXPR simply as "the RMG of EXPR".
             
        ## Subtraction.2
        When we left off, we had the following
                
            eval(expr1 - expr2)
            -> eval(expr1 + (-1)*expr2)
            
        The multiplication rules suffice to solve this. 

        =========================================================
        Implementation
        
        define a mapping
            key: i, j -> slice of num
            value: Set(3-tuple)
                - evaluation possible using operators on slice
                - value of right multiplication group
                - value of left multiplication group
            
        We will use the mapping to solve the recurrence in the following way:
            mapping[i,j], mapping[j,k] -> mapping[i,k]           
        '''
