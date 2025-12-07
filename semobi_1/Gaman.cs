using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Gaman corpse" )]
	public class Gaman : BaseCreature
	{

		[Constructable]
		public Gaman() : base( AIType.AI_Animal, FightMode.Agressor, 10, 1, 0.2, 0.4 )
		{
			Name = "a Gaman";
			Body = 248;
			BaseSoundID = 357;

			SetStr( 145, 175 );
			SetDex( 115, 145 );
			SetInt( 45, 60 );

			SetHits( 130, 160 );
			SetMana( 0, 0 );
			SetStam( 115, 145 );

			SetDamage( 13, 23 );

			SetDamageType( ResistanceType.Physical, 20 ); 

			SetResistance( ResistanceType.Physical, 50, 70 );
			SetResistance( ResistanceType.Fire, 30, 50 );
			SetResistance( ResistanceType.Cold, 30, 50 );
			SetResistance( ResistanceType.Poison, 40, 60 );
			SetResistance( ResistanceType.Energy, 30, 50 );

			SetSkill( SkillName.MagicResist, 35.0, 45.0 );
			SetSkill( SkillName.Tactics, 70.0, 85.0 );
			SetSkill( SkillName.Wrestling, 50.0, 60.0 );
			SetSkill( SkillName.Anatomy, 10.0, 40.0 );

			Fame = 900;
			Karma = 0;
			
			Tamable = true;
			ControlSlots = 1;
			MinTameSkill = 68.7;

	PackGold( 700, 1000 );
	}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 1 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
     	 	public override bool BardImmune{ get{ return true; } }
		public override int Meat{ get{ return 10; } }
		public override int Hides{ get{ return 15; } }
		public override FoodType FavoriteFood{ get{ return FoodType.GrainsAndHay; } }
		public override PackInstinct PackInstinct{ get{ return PackInstinct.Bull; } }

                public Gaman( Serial serial ) : base( serial )
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