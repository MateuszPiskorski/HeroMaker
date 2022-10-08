from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    rule_set = models.CharField(max_length=255, default="classic")


class Characteristics(models.Model):
    fellowship = models.PositiveSmallIntegerField()
    willpower = models.PositiveSmallIntegerField()
    intelligence = models.PositiveSmallIntegerField()
    dexterity = models.PositiveSmallIntegerField()
    agility = models.PositiveSmallIntegerField()
    initiative = models.PositiveSmallIntegerField()
    toughness = models.PositiveSmallIntegerField()
    strength = models.PositiveSmallIntegerField()
    ballistic_skill = models.PositiveSmallIntegerField()
    weapon_skill = models.PositiveSmallIntegerField()


class Class(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Talent(models.Model):
    name = models.CharField(max_length=255)
    tests = models.CharField(max_length=255)
    bonus_when_maxed = models.CharField(max_length=255)
    description = models.TextField()
    level = models.PositiveSmallIntegerField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    characteristic = models.CharField(max_length=255)
    description = models.TextField()

    is_advanced = models.BooleanField(default=False)
    is_grouped = models.BooleanField(default=False)


class Career(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_level_name = models.CharField(max_length=255)

    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    talents = models.ManyToManyField(Talent)
    skills = models.ManyToManyField(Skill)


class Species(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    disallowed_careers = models.ManyToManyField(Career)
    skills = models.ManyToManyField(Skill)
    talents = models.ManyToManyField(Talent)





# class Hero(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.PositiveSmallIntegerField(blank=True)
#     height = models.CharField(max_length=5)
#     hair = models.CharField(max_length=255)
#     eyes = models.CharField(max_length=255)
#     wounds = models.PositiveSmallIntegerField()
#     experience = models.PositiveSmallIntegerField()
#     short_term_ambition = models.CharField(max_length=255)
#     long_term_ambition = models.CharField(max_length=255)
#     brass_pennies = models.PositiveSmallIntegerField()
#     silver_shillings = models.PositiveSmallIntegerField()
#     golden_crowns = models.PositiveSmallIntegerField()
#
#     characteristics = models.OneToOneField(Characteristics)
#     species = models.OneToOneField(Species)
#     class_ = models.OneToOneField(Class)
#     career = models.OneToOneField(Career)
#     game = models.ManyToManyField(Game)
