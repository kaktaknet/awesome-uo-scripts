using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Yomotsu corpse" )]
	public class YomotsuWarrior : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.ParalyzingBlow;
            } 

		[Constructable]
		public YomotsuWarrior() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Yomotsu Warrior";
			Body = 245;
			BaseSoundID = 422;

			SetStr( 480, 530 );
			SetDex( 150, 165 );
			SetInt( 15, 35 );

			SetHits( 480, 530 );
			SetMana( 15, 35 );
			SetStam( 150, 165 );

			SetDamage( 55, 65 );

			SetDamageType( ResistanceType.Physical, 100 ); 
 

			SetResistance( ResistanceType.Physical, 65, 85 );
			SetResistance( ResistanceType.Fire, 30, 50 );
			SetResistance( ResistanceType.Cold, 45, 65 );
			SetResistance( ResistanceType.Poison, 40, 55 );
			SetResistance( ResistanceType.Energy, 30, 50 );

			SetSkill( SkillName.MagicResist, 80.0, 90.0 );
			SetSkill( SkillName.Tactics, 95.0, 105.0 );
			SetSkill( SkillName.Wrestling, 98.0, 108.0 );
			SetSkill( SkillName.Anatomy, 85.0, 95.0 );

			Fame = 5000;
			Karma = -5000;
			
			Tamable = false;

			
         PackGold( 600, 700 ); 
         PackMagicItems( 1, 5 );
			AddItem( new Sandals());
			AddItem( new ExecutionersAxe());
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.Average );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
      	public override bool BardImmune{ get{ return true; } }
		public override FoodType FavoriteFood{ get{ return FoodType.FruitsAndVegies; } }

                public YomotsuWarrior( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}