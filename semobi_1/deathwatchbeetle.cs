using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Deathwatch Beetle corpse" )]
	public class DeathwatchBeetle : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.ArmorIgnore;
            } 

		[Constructable]
		public DeathwatchBeetle() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Deathwatch Beetle";
			Body = 242;
			BaseSoundID = 1006;

			SetStr( 135, 160 );
			SetDex( 40, 55 );
			SetInt( 30, 40 );

			SetHits( 120, 130 );
			SetMana( 20, 20 );
			SetStam( 40, 55 );

			SetDamage( 10, 21 );

			SetDamageType( ResistanceType.Physical, 100 ); 


			SetResistance( ResistanceType.Physical, 35, 40 );
			SetResistance( ResistanceType.Fire, 15, 30 );
			SetResistance( ResistanceType.Cold, 15, 30 );
			SetResistance( ResistanceType.Poison, 50, 80 );
			SetResistance( ResistanceType.Energy, 20, 35 );

			SetSkill( SkillName.MagicResist, 50.0, 60.0 );
			SetSkill( SkillName.Tactics, 65.0, 80.0 );
			SetSkill( SkillName.Wrestling, 50.0, 50.0 );
			SetSkill( SkillName.Anatomy, 30.0, 35.0);


			Fame = 300;
			Karma = 300;
			
			Tamable = true;
			ControlSlots = 1;
			MinTameSkill = 41.1;
			
         PackGold( 1000, 1200 ); 
         PackMagicItems( 1, 5 );
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Greater; } }
		public override Poison HitPoison{ get{ return Poison.Greater; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Meat; } }
		public override int Hides{ get{ return 8; } }
		public override HideType HideType{ get{ return HideType.Horned; } }

                public DeathwatchBeetle( Serial serial ) : base( serial )
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