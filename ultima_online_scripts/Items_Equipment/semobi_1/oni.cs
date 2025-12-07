using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "an Oni corpse" )]
	public class Oni : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public Oni() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "an Oni";
			Body = 241;
			BaseSoundID = 0x9E;

			SetStr( 800, 905 );
			SetDex( 150, 200 );
			SetInt( 170, 200 );

			SetHits( 400, 530 );
			SetMana( 170, 200 );
			SetStam( 150, 200 );

			SetDamage( 57, 99 );

			SetDamageType( ResistanceType.Physical, 70 ); 
	         	SetDamageType( ResistanceType.Fire, 10 ); 
        	 	SetDamageType( ResistanceType.Energy, 20 ); 

			SetResistance( ResistanceType.Physical, 65, 80 );
			SetResistance( ResistanceType.Fire, 50, 70 );
			SetResistance( ResistanceType.Cold, 35, 50 );
			SetResistance( ResistanceType.Poison, 45, 70 );
			SetResistance( ResistanceType.Energy, 45, 65 );

			SetSkill( SkillName.MagicResist, 85.0, 100.0 );
			SetSkill( SkillName.Tactics, 85.0, 100.0 );
			SetSkill( SkillName.Wrestling, 90.0, 100.0 );
			SetSkill( SkillName.Magery, 96.0, 106.0 );
			SetSkill( SkillName.Meditation, 27.5, 42.5 );
			SetSkill( SkillName.EvalInt, 100.0, 125.0 );

			Fame = 15000;
			Karma = -15000;
			
			Tamable = false;

         PackGold( 1600, 1850 ); 
         PackMagicItems( 1, 5 );

		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.FilthyRich );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
		public override FoodType FavoriteFood{ get{ return FoodType.FruitsAndVegies; } }

                public Oni( Serial serial ) : base( serial )
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