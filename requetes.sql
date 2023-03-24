---------------------   5. Créer une table profiles  ---------------------
-- 1. Create table profile
create table public.profiles (
  id uuid not null references auth.users on delete cascade,
  email varchar(50) not null,
  first_name varchar(50) ,
  last_name varchar(50),
  job varchar(50),
  date_of_birth date,
  address varchar(50),
  town varchar(50),
  created_at timestamp with time zone default current_timestamp,

  primary key (id)
);

-- 2. Enable RLS
alter table public.profiles enable row level security;



----  TRIGGER
-- inserts a row into public.profiles
create function public.add_new_user_and_profile()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles (id, email)
  values (
    NEW.id,
    NEW.email
  );
  return new;
end;
$$;

-- when new user created, trigger this function
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.add_new_user_and_profile();


---------------------   6. Créer une table friends qui associe un utilisateur avec un autre utilisateur ami  ---------------------
create table public.friends (
  user1 uuid not null references auth.users on delete cascade,
  user2 uuid not null references auth.users on delete cascade,
  created_at timestamp with time zone default current_timestamp,

  primary key (user1, user2)
);



---------------------   7. Joindre les données profiles, avec les données du user postgresql correspondant (auth.users)  ---------------------
SELECT *
FROM public.profiles p
JOIN auth.users u ON u.id = p.id;



---------------------   8. Implémente le row level security : Implémenter une contrainte Row level security : Un utilisateur ne peut acceder qu’au profile de ses amis. ---------------------

SELECT p.*
FROM public.friends f
JOIN public.profiles p ON p.id = f.user1
WHERE p.id = auth.uid()

------ RLS

create policy "Users can view only friend's profile."
  on public.profiles
  for select using (
    profiles.id in (
      select user2 from public.friends
      where auth.uid() = friends.user1
    )
  );

create policy "Users can see all friend's profile."
on public.profiles
for select
using (
  exists (
    select 1 from public.friends
    where auth.uid() = friends.user1 and profiles.id = friends.user1
  )
);
