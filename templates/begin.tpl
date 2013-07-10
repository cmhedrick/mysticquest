<div>
  <h1>{{title}}</h1>
  <p>{{story}}</p>
</div>

<form action="/moving" method="post">
  <input type="radio" name="direction" value="N" />
  <input type="radio" name="direction" value="E" />
  <input type="radio" name="direction" value="S" />
  <input type="radio" name="direction" value="W" />
  <input type="submit" name="Submit" />
</form> 

%rebase templates/base.tpl title=title
