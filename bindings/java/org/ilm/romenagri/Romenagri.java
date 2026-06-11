package org.ilm.romenagri;
import java.util.*;
/** Romenagri Java binding — table-driven (canonical_basis.json).
 *  Copyright (C) 1993-2026 Abhishek Choudhary. GPL-3.0-or-later. */
public class Romenagri {
  private final Map<Character,String> fwd=new HashMap<>();
  private final TreeMap<String,Character> rev=new TreeMap<>(
      Comparator.comparingInt(String::length).reversed().thenComparing(Comparator.naturalOrder()));
  public Romenagri(List<Map.Entry<String,Character>> basis){
    for(var e:basis){ if(e.getValue()!=0) fwd.put(e.getValue(),e.getKey());
                      if(!e.getKey().isEmpty()) rev.put(e.getKey(),e.getValue()); } }
  public String toRomenagri(String iscii){ StringBuilder b=new StringBuilder();
    for(char c:iscii.toCharArray()) b.append(fwd.getOrDefault(c,String.valueOf(c))); return b.toString(); }
  public String toIscii(String rmn){ StringBuilder b=new StringBuilder(); int i=0;
    outer: while(i<rmn.length()){ for(String k:rev.keySet())
        if(rmn.startsWith(k,i)){ b.append(rev.get(k)); i+=k.length(); continue outer; }
      b.append(rmn.charAt(i++)); } return b.toString(); }
}
