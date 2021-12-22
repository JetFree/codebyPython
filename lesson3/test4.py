string_first = 'четырёхсотпятидесятисемимиллиметровое'
fs_fchar = string_first[0]
fs_lchar = string_first[-1]

string_second = 'метоксихлордиэтиламинометилбутиламиноакридин'
ss_fchar = string_second[0]
ss_lchar = string_second[-1]

string_third = 'автомотовелофототелерадиомонтёр'
ts_fchar = string_third[0]
ts_lchar = string_third[-1]

string_forth = 'автоэлектростеклоподъемники'
fts_fchar = string_forth[0]
fts_lchar = string_forth[-1]

print(string_first, fs_fchar, fs_lchar,
      string_first.count(fs_fchar) + string_first.count(fs_lchar))
print(string_second, ss_fchar, ss_lchar,
      string_second.count(ss_fchar) + string_second.count(ss_lchar))
print(string_third, ts_fchar, ts_lchar,
      string_third.count(ts_fchar) + string_third.count(ts_lchar))
print(string_forth, fts_fchar, fts_lchar,
      string_forth.count(fts_fchar) + string_forth.count(fts_lchar))
