fun twosum ([], _) = NONE
  | twosum (x::xs, target) =
    let fun find (y::ys, i) = if x + y = target then SOME (0, i) else find (ys, i+1)
          | find (_, _) = let val res = twosum(xs, target) in case res of SOME (a, b) => SOME (a+1, b+1) | NONE => NONE end
    in find (xs, 1) end;

(* تست کد *)
val result = twosum ([2, 7, 11, 15], 9);
case result of SOME (i, j) => print ("[" ^ Int.toString i ^ ", " ^ Int.toString j ^ "]\n") | NONE => print "No solution\n";